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
						'background-color' : color,
						'line-color': color,
						'target-arrow-color': color,
					},

					duration: 500,
					easing: "linear"
				});
			},

			generateElements() {
				const elements = [];

				for (const fn of this.analysis.functions) {
					elements.push({
						data: {
							id: fn
						}
					});
				}

				for (const [caller, callee] of this.analysis.edges) {
					elements.push({
						data: {
							id: `${caller}-${callee}`,
							source: caller,
							target: callee
						}
					});
				}

				return elements;
			},

			onNodeTapped(function_name) {
				// console.log(function_name);
			}
		},

		mounted() {
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
