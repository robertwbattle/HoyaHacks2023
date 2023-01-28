<template lang="en">
    <div class="fileform">
            <form method="POST" :action=url enctype=multipart/form-data>
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
    }
}
</script>
<style lang="">
    
</style>