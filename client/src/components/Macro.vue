<template>
  <div class="macro-container">
    <div id="cy"></div>
    <div class="macro-player">
      <button id="pause" class="playback-btn btn btn-secondary">Pause</button>
      <button id="play" class="playback-btn btn btn-secondary">Play</button>
    </div>
  </div>
</template>

<script>
import macroJSON from '../json/exampleData.json'
import cytoscape from 'cytoscape';

export default {
  name: 'Macro',
  props: {
  },
  components: {
    Function
  },
  data() {
    return {
      macroData: []
    }
  },
  methods: {
    async updateMacro() {
      let cyto = []
      Object.values(macroJSON.functions).forEach(val => {
        const container = {};
        container.data = {
          id: val
        };
        cyto.push(container)
      });
      macroJSON.edges.forEach(edge => {
        const container = {};
        const edgeStart = macroJSON.functions[edge[0]];
        const edgeEnd = macroJSON.functions[edge[1]];
        container.data = {
          id: edgeStart+ '-' + edgeEnd,
          source: edgeStart,
          target: edgeEnd
        };
        cyto.push(container)
      });
      return cyto
    },
    setUpGraph() {
      let cy = cytoscape({
      container: document.getElementById('cy'),
      elements: this.macroData,
      style: [ // the stylesheet for the graph
          {
            selector: 'node',
            style: {
              'background-color': '#FBF9FF',
              'label': 'data(id)'
            },
            css: {
              events: 'no'
            }
          },
          {
            selector: 'edge',
            style: {
              'width': 3,
              'line-color': '#ccc',
              'target-arrow-color': '#ccc',
              'target-arrow-shape': 'triangle',
              'curve-style': 'bezier'
            }
          },
          // {
          //   selector: '.foo',
          //   style: {
          //     'background-color': '#000'
          //   }
          // }
        ],
      });
      cy.userZoomingEnabled( false );

      cy.on('tap', 'node', function (evt) {
          // console.log(evt.target.id());
          // console.log(evt.target);
          // evt.target.toggleClass('foo')
      });

      let animationQueue= []
      for(let i = 0; i < macroJSON.order.length; i++) {
        if(i == macroJSON.order.length - 1) {
          break
        }
        let sourceNode = cy.elements(`node#${macroJSON.order[i]}`);
        let targetNode = cy.elements(`node#${macroJSON.order[i+1]}`);
        let edge = sourceNode.edgesTo(`#${macroJSON.order[i+1]}`);
        animationQueue.push(sourceNode.id());
        animationQueue.push(edge.id());
      }
      console.log(animationQueue)
      
      this.animateNode(cy, animationQueue, 0, false);
      setTimeout(this.animateNode(cy, animationQueue, 0, true), 1000)
    },
    animateNode(cy, queue, i, isFading) {
      if (i >= queue.length) {
        return
      }
        let color;
        const elmId = queue[i];
        const currentElm = cy.elements(`#${elmId}`);
        //console.log(currentElm)
        
        if(isFading){
          color = '#FBF9FF'
        }
        else {
          color = '#ff6933'
        }
        currentElm.animate({
            style : {
              'background-color' : color
            },
            duration: 1000,
            easing: 'linear'
          }, 1000)
        

        setTimeout(() => this.animateNode(cy, queue, i + 1, isFading), 250,)
      }
  },
  async mounted() {
    this.macroData = await this.updateMacro();
    await this.setUpGraph()
  }
}
</script>

<style scoped>
#cy {
  width: 50vw;
  height: 50vh;
  display: block;
}
.macro-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.playback-btn {
  margin: 0 10px;
}
</style>