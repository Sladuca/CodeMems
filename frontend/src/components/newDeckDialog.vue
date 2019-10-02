<template>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on }">
        <v-btn text v-on="on">New Deck</v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">New Deck</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field label="Deck Name" v-model="deckName" required></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <div class="flex-grow-1"></div>
          <v-btn text @click="closeDialog()">Cancel</v-btn>
          <v-btn text @click="onSave()">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>
import { mapActions } from "vuex"
export default {
  name: "newDeckDialog",
  data: () => {
    return {
      dialog: false,
      deckName: "",
    }
  },
  methods: {
    ...mapActions([
      "addDeck",
    ]),
    closeDialog() {
      this.dialog = false
    },
    onSave(e) {
      // hardcode these for now
      const newDeck = {
        "_id": Math.random() * (999999 - 1000) + 1000,
        "userId": 0,
        "title": this.deckName,
        "numToReview": 0,
      }
      this.closeDialog()
      this.addDeck(newDeck)
    },
  },
}
</script>
