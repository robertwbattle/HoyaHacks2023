<template>
  <div class="main-container">
    <!-- <Micro /> -->
    <FileForm url="http://127.0.0.1:5000/analyze"></FileForm>
    <span class="line"></span>
    <Macro/>
  </div>
</template>

<script>
  import Macro from './components/Macro'
  import Micro from './components/Micro'
  import Index from './components/Index.vue'
  import FileForm from './components/FileForm.vue'


export default {
  name: 'App',
  components: {
    Macro,
    Micro,
    Index,
    FileForm
  },
  data() {
    return {
      micro: []
    }
  },
  methods: {
    
  },
  async mounted() {
  }

}
</script>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.main-container {
  display: grid;
  width: auto;
  height: 100%;
  grid-template-columns: 50% auto 50%;
  background-color: #262626;
}

.line {
  background:linear-gradient(#000,#000) center/2px 100% no-repeat;
  height: 100vh;
  width: 1px;
}
</style>
