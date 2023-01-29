<template>
    <div class="micro-container">
        <textarea readonly cols="30" id="json" style="background-color: transparent;color:#fff;width: 100%; height: 75%;resize:none;"></textarea>
        <label class="path-label" for="path-input">Enter variable to track in the format function/variable/functionCall, then press view!</label>
        <input type="text" name="path-input" id="path-input" placeholder="bar/z/0" style="resize:none;height:30px;width: 100%;background-color:transparent;color:#fff;">
    </div>
</template>

<script>
    import createStates from '../createStates';
    export default {
        name: "Micro",
        props: ["analysis"],
        methods: {
            insertJson(txt) {
                document.getElementById("json").value = JSON.stringify(createStates(txt.microscopic), undefined, 4);
            }
        },
        mounted() {
            this.insertJson(this.analysis)
        }
    }
</script>

<style scoped>
.micro-container {
    display: flex;
    flex-direction: column;
}
.path-label {
    color: #FBF9FF;
}
</style>