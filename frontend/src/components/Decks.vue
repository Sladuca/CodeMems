<template>
<!-- Deck items --> 
  <v-expansion-panels
    class="pa-4 md-4"
    >
    <v-expansion-panel
      v-for="(item, i) in 3"
      :key="i"
    >
    <v-expansion-panel-header>
      <v-badge
        :left=true
        >
        <template v-slot:badge>33</template>
        <span>Deck_Name</span>
      </v-badge>
    </v-expansion-panel-header>
    <v-expansion-panel-content>
      Review
    </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: "Decks",
  methods: {
    ...mapActions([
      "addDeck",
      "addNote",
      "updateNote",
    ]),
    ...mapGetters([
      "getDecks",
      "getNotes",
    ]),
  }
}
</script>
