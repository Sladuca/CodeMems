import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const viewModule = {
  state: {
    current_view: "welcome",
  },
  mutations: {
    changeView (state, newView) {
      state.current_view = newView
    }
  },
  getters: {
    currentView: state => {
      return state.current_view
    },
  },
  actions: {
    changeView (context, newView) {
      context.commit('changeView', newView)
    },
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

export default new Vuex.Store({
  modules: {
    view: viewModule,
    decks: decksModule,
    cards: cardsModule,
    profile: profileModule,
    stats: statsModule
  },
})
