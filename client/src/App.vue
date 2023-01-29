<template>
    <div class="main-container">
        <Micro v-if="this.analysis"/>
        <FileForm v-else="this.analysis" url="/analyze" @received-analysis="setAnalysis"></FileForm>

        <span class="line"></span>

        <Macro v-if="this.analysis"/>
    </div>
</template>

<script>
    import FileForm from "./components/FileForm.vue"
    import Macro from "./components/Macro"
    import Micro from "./components/Micro"

    export default {
        name: "App",
        components: {
            FileForm,
            Macro,
            Micro
        },

        data() {
            return {
                analysis: null
            }
        },

        methods: {
            setAnalysis(analysis) {
                this.analysis = analysis;
            }
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
