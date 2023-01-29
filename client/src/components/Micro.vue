<template>
	<Canvas
		:generateElements="this.generateElements"
		:onNodeTapped="this.onNodeTapped"
		ref="canvas"></Canvas>
</template>

<script>
	import Canvas from "./Canvas";

    export default {
        name: "Macro",
        props: ["analysis"],
        components: {
            Canvas
        },

        methods: {
			animateElement(element, shouldFade) {
				let color;

				if (shouldFade) {
					color = this.$refs.canvas.backgroundColor();
				} else {
					color = "#FF6933";
				}

				element.animate({
					style : {
						"background-color" : color
					},

					duration: 100,
					easing: "linear"
				});
			},

			generateElements(funcName) {
				const elements = [];
        for (const elm of this.analysis.microscopic.funcName){
          if(elm.type === "list"){
            elements.push({
              data: {
                id: elm.name
              }
            })
            // for(const info in elm.invocation){

            // }
            console.log(elm.invocations[0])
            console.log(elm.invocations[0].inital_value)

            for(listElm of elm.invocations[0]["inital_value"]){
              elements.push({
                data: {
                  id: listElm,
                  parent: elm.name
                }
              });
            }
          }
          if(this.analysis.microscopic.fizz[0].type == "list"){
            console.log(`${this.analysis.microscopic.fizz[0].name} is a list!`)
          }
          console.log(this.analysis.microscopic.fizz[0].type)
          console.log(elements)
        }
        console.log(elements)

				// for (const [caller, callee] of this.analysis.edges) {
				// 	elements.push({
				// 		data: {
				// 			id: `${caller}-${callee}`,
				// 			source: caller,
				// 			target: callee
				// 		}
				// 	});
				// }

				// return elements;
			},

			onNodeTapped(function_name) {
				console.log(function_name);
			}
		},

		mounted() {
      console.log(this.analysis)
			let shouldFade = false;

			do {
				if (shouldFade) {
					this.$refs.canvas.addAnimation(() => {});
				}

				for (let i = 0; i < this.analysis.order.length; i++) {
					const currentShouldFade = shouldFade;

					this.$refs.canvas.addAnimation(canvas => {
						const node = canvas.elements(`node#${this.analysis.order[i]}`);

						this.animateElement(node, currentShouldFade);

						if (i < this.analysis.order.length - 1) {
							this.animateElement(
								node.edgesWith(`#${this.analysis.order[i + 1]}`),
								currentShouldFade
							);
						}
					});
				}

				shouldFade = !shouldFade;
			} while(shouldFade);

			this.$refs.canvas.render();
		}
    }
</script>