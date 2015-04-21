#include <mbgl/map/resource_loader.hpp>

#include <mbgl/geometry/sprite_atlas.hpp>
#include <mbgl/map/environment.hpp>
#include <mbgl/map/map.hpp>
#include <mbgl/map/source.hpp>
#include <mbgl/map/sprite.hpp>
#include <mbgl/style/style.hpp>
#include <mbgl/util/worker.hpp>

#include <cassert>
#include <cstddef>

namespace {

const std::size_t threadPoolSize = 4;

}

namespace mbgl {

ResourceLoader::ResourceLoader() : observer_(nullptr) {
    assert(Environment::currentlyOn(ThreadType::Map));

    // The worker pool will reply to the Map thread main loop,
    // so we have to make sure this object outlives the Map thread.
    worker_ = util::make_unique<Worker>(Environment::Get().loop, threadPoolSize);
}

ResourceLoader::~ResourceLoader() {
    assert(Environment::currentlyOn(ThreadType::Map));

    sprite_->setObserver(nullptr);
}

void ResourceLoader::setObserver(Observer* observer) {
    assert(Environment::currentlyOn(ThreadType::Map));
    assert(!observer_);

    observer_ = observer;
}

void ResourceLoader::setStyle(util::ptr<Style> style) {
    style_ = style;

    Environment& env = Environment::Get();
    for (const auto& source : style->sources) {
        source->setObserver(this);
        source->load(accessToken_, env);
    }
}

void ResourceLoader::setAccessToken(const std::string& accessToken) {
    accessToken_ = accessToken;
}

void ResourceLoader::update(Map& map,
                           GlyphAtlas& glyphAtlas,
                           GlyphStore& glyphStore,
                           SpriteAtlas& spriteAtlas,
                           TexturePool& texturePool) {
    if (!style_) {
        return;
    }

    const float pixelRatio = map.getState().getPixelRatio();
    if (!sprite_ || !sprite_->hasPixelRatio(pixelRatio)) {
        sprite_ = Sprite::Create(style_->getSpriteURL(), pixelRatio);
        sprite_->setObserver(this);

        spriteAtlas.resize(pixelRatio);
        spriteAtlas.setSprite(sprite_);
    }

    for (const auto& source : style_->sources) {
        source->update(
            map, *worker_, style_, glyphAtlas, glyphStore, spriteAtlas, sprite_, texturePool);
    }
}

void ResourceLoader::onSourceLoaded() {
    emitTileDataChanged();
}

void ResourceLoader::onTileLoaded() {
    emitTileDataChanged();
}

void ResourceLoader::onSpriteLoaded() {
    emitTileDataChanged();
}

void ResourceLoader::emitTileDataChanged() {
    assert(Environment::currentlyOn(ThreadType::Map));

    if (observer_) {
        observer_->onTileDataChanged();
    }
}

}
