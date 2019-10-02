<template>
<!-- Deck items --> 
  <v-expansion-panels
    class="pa-4 md-4"
    >
    <v-expansion-panel
      v-for="(deck, i) in allDecks"
      :key="i"
    >
    <v-expansion-panel-header>
      <v-badge
        :left=true
        >
        <template v-slot:badge>{{ i }}</template>
        <span>{{ deck.title }}</span>
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
      "getDecks",
    ]),
  },
  computed: {
    ...mapGetters([
      "allDecks",
    ]),
  },
  created() {
    this.getDecks();
  },
}
</script>
