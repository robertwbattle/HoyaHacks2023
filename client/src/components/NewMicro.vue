<template>
    <div class="micro-container">
        <textarea readonly cols="30" id="json"></textarea>
        <label for="string-parser" class="parser-label">Enter variable to track in the format function/variable/functionCall, then press view!</label>
        <input type="text" id="string-parser" name="string-parser" placeholder="pizzaCounter/cheesePizzas/0">
        <button id="view" @click="view" class="btn btn-caution">View</button>
        <p style="" id="variable"></p>
        <div>
            <button style="margin-top:100px" id="back" @click="back" class="btn btn-primary">Back</button>
            <button style="margin-top:100px;margin-left:20px;" id="forward" @click="forward" class="btn btn-primary">Forward</button>
        </div>
        <p hidden id="currentState"></p>
        <p hidden id="cind"></p>
    </div>
</template>

<script>
    import createStates from '../createStates';
    export default {
        name: "Micro",
        props: ["analysis"],
        methods: {
            insertJson(txt) {
                var states = createStates(txt.microscopic)
                document.getElementById("json").value = JSON.stringify(states, undefined, 4);
            },
            view() {
                console.log("viewed")
                var output = document.getElementById("enter").value.split("/");
                console.log(output)
                if (JSON.parse(document.getElementById("json").value)[output[0]][output[1]][output[2]]) {
                    document.getElementById("currentState").innerHTML = JSON.stringify(JSON.parse(document.getElementById("json").value)[output[0]][output[1]][output[2]]);
                    document.getElementById("cind").innerHTML = 0;
                    document.getElementById("variable").innerHTML = JSON.stringify(JSON.parse(document.getElementById("json").value)[output[0]][output[1]][output[2]][0]);
                }
            },
            forward() {
                var cind = document.getElementById("cind").innerHTML;
                var d = JSON.parse(document.getElementById("currentState").innerHTML);
                cind = cind < d.length-1 ? cind + 1 : cind;
                console.log(cind);
                console.log(JSON.parse(document.getElementById("currentState").innerHTML))
                document.getElementById("variable").innerHTML = JSON.stringify(JSON.parse(document.getElementById("currentState").innerHTML)[parseInt(cind, 10)]);
            },
            back() {
                var cind = document.getElementById("cind").innerHTML;
                cind = cind > 0 ? cind - 1 : cind;
                document.getElementById("variable").innerHTML = JSON.stringify(JSON.parse(document.getElementById("currentState").innerHTML)[parseInt(cind, 10)]);

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

.parser-label {
    color: #FBF9FF;
}

#json {
    height: 70%;
    background-color: transparent;
    color: #FBF9FF;
}
</style>