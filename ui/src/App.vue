<template>
  <div id="app">
    <showPoem />
  </div>
</template>

<script>
import showPoem from './components/showPoem.vue'

export default {
  name: 'app',
  components: {
      showPoem
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
