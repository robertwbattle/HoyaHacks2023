<template>
  <div class="main-container">
    <!-- <Micro /> -->
    <p>fuidwsbdiusbfiuds</p>
    <span class="line"></span>
    <p>fwiybdisubiuds</p>
    <!-- <Macro /> -->
  </div>
</template>

<script>
  import Macro from './components/Macro'
  import Micro from './components/Micro'

  import {parseJSON} from '@msagl/parser'
  import {Renderer} from '@msagl/renderer'

  import macroJSON from './json/exampleData.json'

export default {
  name: 'App',
  components: {
    Macro,
    Micro
  },
  data() {
    return {
      macroData: [],
      micro: []
    }
  },
  methods: {
    // async fetchMacro() {
    //   const res = await fetch('http://localhost:5000/api/functions');
    //   const data = await res.json();
    //   return data;
    // },
    // async fetchMicro(funcName) {
    //   const res = await fetch(`http://localhost:5000/api/functions/${funcName}`);
    //   const data = await res.json();
    //   return data;
    // },
      async updateMacro() {
        let order = macroJSON.order
        delete macroJSON.order


        console.log(order)

        console.log(macroJSON)

        // const renderer = new Renderer(container?: HTMLDivElement)
        // const graph = parseJSON({
          // nodes: [{id: 'kspacey'}, {id: 'swilliams'}, {id: 'kbacon'}, {id: 'bpitt'}, {id: 'hford'}, {id: 'lwilson'}],
          // edges: [
          //   {source: 'kspacey', target: 'swilliams'},
          //   {source: 'swilliams', target: 'kbacon'},
          //   {source: 'bpitt', target: 'kbacon'},
          //   {source: 'lwilson', target: 'kbacon'},
          // ],
        // })
        // renderer.setGraph(JSON.stringify(macroJSON))
      }
  },
  async created() {
    this.macroData = await this.updateMacro();
  }

}
</script>

<style>
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
  background-color: #FBF9FF;
}

.line {
  background:linear-gradient(#000,#000) center/2px 100% no-repeat;
  height: 100vh;
  width: 1px;
}
</style>
