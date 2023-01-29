<template>
    <div class="d-flex align-items-center justify-content-center">
        <form class="file-upload-form border p-4 rounded" v-on:submit="submitFile" ref="fileUploadForm">
            <h5 class="text-dark mb-4">Upload a Python file to analyze</h5>

            <input type="file" class="form-control mb-3" name="file" required>

            <button type="submit" class="btn btn-primary w-100">Submit</button>
        </form>
    </div>
</template>

<script>
import createStates from '../createStates.js'

export default {
    name: 'FileForm',
    props: {
        url: String
    },

    methods: {
        submitFile(event) {
            fetch(this.url, {
                method: "POST",
                body: new FormData(this.$refs.fileUploadForm)
            })
                .then(response => response.json())
                .then(result => {
                    this.$emit("receivedAnalysis", result);
                    var compiledData = createStates(result["microscopic"]);
                });

            event.preventDefault();
        }
    }
}
</script>

<style scoped>
    .file-upload-form {
        background-color: #f0f0f0;
    }
</style>
