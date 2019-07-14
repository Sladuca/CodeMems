<template lang="html">
  <div class="">
    <div v-for="note in allNotes">
      <Card v-bind:note="note"/>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import Card from './Card.vue'
export default {
  name: "AllCards",
  components: {
    Card
  },
  computed: mapGetters(["allNotes"])
}
</script>

<style lang="css" scoped>
</style>
