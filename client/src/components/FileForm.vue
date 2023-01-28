<template lang="en">
    <div class="fileform">
            <form v-on:submit="sendReq" enctype=multipart/form-data>
                <input type="file" accept=".py" name=file >
                <input type="submit"></input>
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
        async sendReq(evt) {
            let response = await fetch(this.url, {
                method: "POST",
                body: evt.target.file
            });

            let result = await response.json();
        }
    }
}
</script>
<style lang="">
    
</style>