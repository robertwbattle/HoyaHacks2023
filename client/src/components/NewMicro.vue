<template>
    <div style="margin-left:10px"><textarea readonly cols="30" id="json" style="background-color: transparent;color:#fff;height:400px;width:700px;resize:none;"></textarea>
        <p></p>
        <textarea style="resize:none;width:800px;height:30px;background-color:transparent;color:#fff;" maxlength="80">Enter variable to track in the format function/variable/functionCall, then press view!</textarea>
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