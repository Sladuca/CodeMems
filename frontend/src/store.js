import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

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
    changeView(context, newView) {
      context.commit('changeView', newView)
    },
  }
}

const decksModule = {
  state: {
    decks: [
      {
        "title": "NumPy",
        "id": 101,
        "userID": 1,
      },
      {
        "title": "Rust",
        "id": 102,
        "userID": 1,
      },
      {
        "title": "Vue.js",
        "id": 103,
        "userID": 1,
      },
    ],
    nDecks: 3,
  },
  mutations: {
    setDecks: (state, decks) => (state.decks = decks) ,
  },
  getters: {
    allDecks: state => {
      return state.decks
    },
    allNotes: state => {
      return "unimplemented"
    }
  },
  actions: {
    async addDeck(context, newDeck) {},
    async addNote(context, newNote) {},
    async updateNote(context, noteId) {},
    async getDecks(context) {
      const res = await axios.get(
        "https://jsonplaceholder.typicode.com/albums"
      )
    context.commit('setDecks', res.data)
    },
  },
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
