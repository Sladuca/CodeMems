<template lang="html">
  <div class="">
    <div v-for="card in note.data.cards">
      <cv-tile>
        <p>{{card[0]}}</p>
        <p>{{card[1]}}</p>
      </cv-tile>
    </div>
  </div>
</template>

<script>
export default {
  name: "Card",
  props: ["note"]
}
</script>

<style lang="css" scoped>
</style>
