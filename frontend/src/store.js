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
  state: {
    loading: false,
    current_view: "Welcome",
    drawer_open: false,
  }
}

const decksModule = {

}

const cardsModule = {

}

const profileModule = {

}

const statsModule = {

}
