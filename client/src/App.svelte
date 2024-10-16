<script>
	import FileUpload from './FileUploader.svelte';
	import Form from './Form.svelte';
	
</script>

<FileUpload on:change={() => console.log("Files changed")} callback={() => alert("Thanks")}></FileUpload>