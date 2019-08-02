import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    view: viewModule,
    decks: decksModule,
    cards: cardsModule,
    profile: profileModule,
    stats: statsModule
  },
})

const viewModule = {

}

const decksModule = {

}

const cardsModule = {

}

const profileModule = {

}

const statsModule = {

}
