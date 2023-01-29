<template>
	<div class="canvas-container position-relative">
		<div class="canvas w-100 h-100" ref="canvas"></div>

		<div class="player d-flex position-absolute">
			<button class="btn btn-secondary me-2">Pause</button>
			<button class="btn btn-secondary">Play</button>
		</div>
	</div>
</template>

<script>
	import cytoscape from "cytoscape";
	import autopanOnDrag from "cytoscape-autopan-on-drag";
	autopanOnDrag( cytoscape ); // register extension

    export default {
        name: "Canvas",
        props: ["generateElements", "onNodeTapped"],

		data() {
			return {
				animations: [],
				canvas: null
			}
		},

        methods: {
            addAnimation(callback) {
				this.animations.push(callback);
			},

			backgroundColor() {
				return "#FBF9FF";
			},

            render() {
				let animation = () => {};

				for (let i = this.animations.length - 1; i >= 0; i--) {
					const current_animation = animation;

					animation = () => {
						this.animations[i](this.canvas);

						current_animation();
					}

					if (i > 0) {
						const current_animation = animation;

						animation = () => this.canvas.delay(1000, current_animation);
					}
				}

				animation();
			},

			setupCanvas() {
				this.canvas = cytoscape({
					container: this.$refs.canvas,
					elements: this.$props.generateElements(),
					style: [
						{
							selector: "node",
							style: {
								"color": "#FBF9FF",
								"background-color": this.backgroundColor(),
								"label": "data(id)"
							},

							css: {
								events: "no"
							}
						},

						{
							selector: "edge",
							style: {
								"curve-style": "bezier",
								"line-color": "#ccc",
								"target-arrow-color": "#ccc",
								"target-arrow-shape": "triangle",
								"width": 3
							}
						},
					],
					layout: {
            'name': 'circle'
					}
				});
				this.canvas.elements().layout({
					name: 'circle'
				});
				this.canvas.on("tap", "node", event => this.$props.onNodeTapped(event.target.id()));
				let instance = this.canvas.autopanOnDrag( 
					{
						enabled: true, // Whether the extension is enabled on register
						selector: 'node', // Which elements will be affected by this extension
						speed: 1 // Speed of panning when elements exceed canvas bounds
					}
				);
				instance.enable(); // enable the instance
				this.canvas.autopanOnDrag('get');
				
			}
        },

		mounted() {
			this.setupCanvas();
		}
    }
</script>

<style scoped>
	.canvas-container {
		width: 50vw;
	}

	.container {
		position: relative;
	}

	.player {
		bottom: 1rem;
		justify-content: center;
		position: absolute;
		width: 50vw;
	}
</style>
