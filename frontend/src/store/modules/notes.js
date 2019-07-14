const state = {
  notes: [
    {
      notetype: "CARD",
      data: {
        fields: [
          {"Country": "Peru"},
          {"Capital": "Lima"}
        ],
        cards: [
          ["Country", "Capital"],
          ["Capital", "Country"],
        ]
      }
    }
  ],
};

const getters = {
  allNotes: (state) => state.notes,
}

const actions = {
  async addNote({commit}, note) {
    let newNote = {
      notetype: "CARD",
      data: {
        fields: [
          {"Front": note.front},
          {"Back": note.back},
        ],
        cards: [
          ["Front", note.back],
          ["Back", note.front],
        ]
      }
    }
    commit('newNote', newNote)
  }
}

const mutations = {
  newNote: (state, note) => state.notes.unshift(note),
}

export default {
  state,
  getters,
  actions,
  mutations,
}
