<template lang="en">
    <div class="d-flex align-items-center justify-content-center">
        <form class="file-upload-form p-4 rounded" v-on:submit="submitFile" ref="fileUploadForm">
            <h5 class="text-dark mb-4">Upload a Python file to analyze</h5>

            <input type="file" class="file-upload-input form-control mb-3" name="file">

            <button type="submit" class="btn btn-primary w-100">Submit</button>
        </form>
    </div>
</template>

<script>

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
                .then(result => console.log(result));

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
