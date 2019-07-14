<template lang="html">
  <div class="">
    <cv-form>
      <cv-text-input label="Front" v-model="front" placeholder="e.g. Capital of USA" />
      <cv-text-input label="Back" v-model="back" placeholder="e.g. Washington D.C." />
      <cv-button @click="clickAddNote">Add</cv-button>
    </cv-form>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
export default {
  name: "AddNote",
  data() {
    return {
      front: "",
      back: "",
    }
  },
  methods: {
    ...mapActions(['addNote']),
    clickAddNote(event){
      event.preventDefault();
      this.addNote(this);
      this.front = "";
      this.back = "";
    }
  }
}
</script>

<style lang="css" scoped>
</style>
