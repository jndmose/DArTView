<script>
import icons from "./icons.js";
import Controller from './Controller.js';
import ListDisplay from './ListDisplay.svelte';
   

 let buttonText = "Upload";
  
  let descriptionText = "No Marker Data Loaded, Drag or click to upload";
 
 //Fixed uploader position?
  let fixed = true;
  let dragZoneFile= null;
 //Trigger file upload
 $: runUpload =  () => {
      
	  const upload=   document.getElementById("upload");
	  
	  upload.click();
	  return false;

   }

 // Drag zone element
  let dragZone = null;


 const controller = new Controller();
 import {geno_data, marker_metadata, sample_list,marker_list} from './data.js';


 let sampleNumber = 0;

 async function openFile(fl){ 
	$geno_data = await controller.openFile(fl);
	if($geno_data instanceof Error){
		hasError= true;
	}
  else{
    $marker_metadata= $geno_data.pop();
    $sample_list = $geno_data.pop();
    $marker_list= $geno_data.pop();

  }
	
	sampleNumber = $geno_data[0].length;
   }
 
 import {createEventDispatcher} from "svelte";
 
 const dispatch = createEventDispatcher();
 
 function dragover(e){
     e.preventDefault();
     dispatch("dragover", e);
 }
 function dragenter(e){
     e.preventDefault();
     dragZone.classList.add("dragging");
     dispatch("dragenter", e);
 }
 function dragleave(e){
     e.preventDefault();
     dragZone.classList.remove("dragging");
     dispatch("dragleave", e);
 }
 function drop(e){
     e.preventDefault();
     dragZone.classList.remove("dragging");
     dragZoneFile= [...e.dataTransfer.items].filter(i => i.kind === "file").map(i => i.getAsFile());
     console.log(dragZoneFile[0]);
	 openFile(dragZoneFile[0]);
     dispatch("drop", e);
     dispatch("change", files)
 }



</script>


{#if $geno_data.length===0}
<div bind:this={dragZone} on:dragover={dragover} on:drop={drop} on:dragenter={dragenter} on:dragleave={dragleave} class={`${fixed ? 'fixed' : ''} fileUploader dragzone`}>

       <div class="buttons">
          <button on:click={runUpload} class="upload">
             {buttonText}
          </button>
          
       </div>
       {#if descriptionText}<span class="text">{descriptionText}</span>{/if}
   
 </div>
 <input id="upload" hidden type="file"  on:change={openFile} value=""/>


 {:else}
 <ListDisplay />
 {/if}

 <style>
    .dragzone {
		padding: 20px;
		border-radius: 6px;
		border: 2px dashed #0001;
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
		transition: background-color .3s ease;
	}
	
	.dragzone.dragging {
		background: #0662;
	}
	
	.deleteicon {
		display: none;
	}
	
	.dragzone.fixed {
		position: fixed;
		height: 60vh;
		width: 80vw;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
	}
	.dragzone .text {
		font-style: italic;
		color: #333;
		opacity: .5;
		font-weight: 200;
	}

    .buttons {
		width: 40%;
		display: flex;
	}

    .buttons button {
		margin: 0 5px;
		transition: background-color .2s ease;
		padding: .5rem 1rem;
		margin-bottom: 1rem;
		flex: 1;
		border: 1px solid #34c279;
		background: transparent;
		cursor: pointer;
	}
	.buttons button:hover {
		background: #0001;
	}
 </style>









