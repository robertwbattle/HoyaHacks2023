<template>
  <Index msg="Test!"/>
  <p> Howdy!</p>
  <FileForm url="http://127.0.0.1:5000/catch"></FileForm>
</template>

<script>
import Index from './components/Index.vue'
import FileForm from './components/FileForm.vue'

export default {
  name: 'App',
  components: {
    Index,
    FileForm
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
