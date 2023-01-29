<template lang="en">
    <div class="fileform">
            <form v-on:submit="sendReq" enctype=multipart/form-data>
                <input type="file" accept=".py" name=file >
                <input type="submit">
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
        sendReq(event) {
            let fData = new FormData();
            var input = document.querySelector('input[type="file"]');
            fData.append('file', input.files[0])
            fetch(this.url, {
                method: "POST",
                body: fData
            }).then(response=>response.json()).then(result=>console.log(result));
            event.preventDefault();
        }
    }
}
</script>
<style lang="">
    
</style>