<script>
import VirtualList from './VirtualList.svelte';
import Controller from './Controller.js';
import Zoom from './Zoom.svelte';
import { writable } from 'svelte/store';
import Modal, { bind } from 'svelte-simple-modal';
import Sort from './Sort.svelte';
  
let start;
let end;
export let geno_data = [];
const controller = new Controller();
let zoomin = true;
let zoomout= false;
let selected = "zoomin"

let styles = {
		'allele2': '#e74c3c',
		'allele1': '#2ecc71',
		'allele0': '#3498db',
      'allele-': '#f0f8ff'
	};

   $: cssVarStyles = Object.entries(styles)
		.map(([key, value]) => `--${key}:${value}`)
		.join(';');

   //  async function sortData() {
	// geno_data = await controller.sortData();
	
   // }

   function zoom(){

    selected = event.currentTarget.value;
    console.log("selected is", selected)
    if(selected==="zoomin"){
        zoomin=true;
        zoomout= false
    }
    else{
        zoomin= false;
        zoomout=true;
    }
    
   }

  
   const modal = writable(null);
  const sortData = () => modal.set(bind(Sort, { data: geno_data }));


</script>
<div id='geno-map'  style="{cssVarStyles}">

<div class="controls">
	<span> Samples : {geno_data[0].length}</span> &nbsp; <span>Markers : {geno_data.length}</span> &nbsp;
	<!-- <button class="top-buttons" on:click={sortData} > Sort Data</button> -->
   <Modal show={$modal}>
      <button on:click={sortData}>Sort Data</button>
    </Modal>
	<label>
	  <input style="padding:0" type="color" bind:value={styles['allele2']} />
	  Hets
   </label>
   
   <label>
	  <input style="padding:0" type="color" bind:value={styles['allele0']} /> 
	  Hom0
   </label>
   
	  <label>
	  <input style="padding:0" type="color" bind:value={styles['allele1']} /> 
		 Hom1
	  </label>
   
	  <label>
		 <input style="padding:0" type="color" bind:value={styles['allele-']} /> 
			Missing
		 </label>

         <label>
            <input checked={selected==="zoomout"} type="radio" on:change={zoom} name="zoom" value="zoomout" /> Zoom Out
        </label>
        <label>
            <input checked={selected==="zoomin"} type="radio" on:change={zoom} name="zoom" value="zoomin" /> Zoom In
        </label>

       
	</div>

{#if zoomout}
    <Zoom  cssVarStyles= {cssVarStyles} data = {geno_data}/>
{:else}

<VirtualList  items= {geno_data} bind:start bind:end let:item>
    <div class="row-data">
     {#each item as score}
      <span  class="allele{score} data">{score}</span>
      {/each}

      
   </div>
   
   </VirtualList>
   <div class="footer"><p>Showing {start}-{end} of {geno_data.length} Markers</p></div>
   {/if}
   
    </div>

   
   

   <style>

.row-data{
      display: flex;
      border-bottom: 1pt solid #bebebe ;
      
      
   }
 

   .allele0{
      background-color: var(--allele0, #3498db);
   }

   .allele1{
      background-color: var(--allele1,#2ecc71);
   }

   .allele2{
      background-color: var(--allele2,#e74c3c);
   }

   .allele-{
      background-color: var(--allele-,aliceblue);

   }
   .alleleid{
      display: block;
   }

   .data{
      font-family: 'Source Code Pro', monospace;
      text-align: center;
      min-height: 20px;
      min-width: 20px;
      align-items: center;
      justify-content: center;
      border-radius: 1px;
      font-size: 13px;
      display: flex;

   }

   .footer{
	margin-bottom: 5px;
	margin-top: 5px;
	font-family: 'Source Code Pro', monospace;
    text-align-last: center;
   }

   .top-buttons{
	display: inline-block;
                outline: 0;
                cursor: pointer;
                border: none;
                padding: 0 56px;
                height: 45px;
                line-height: 45px;
                border-radius: 7px;
                font-weight: 400;
                font-size: 16px;
                color: #696969;
                box-shadow: 0 4px 14px 0 rgb(0 0 0 / 10%);
                transition: background 0.2s ease,color 0.2s ease,box-shadow 0.2s ease;
   }

   .top-buttons:hover{

	background: rgba(255,255,255,0.9);
	box-shadow: 0 6px 20px rgb(93 93 93 / 23%);

   }

   #geno-map {
      width: 100%;
	  padding: 20px;
	  height: calc(105vh - 15em);
      max-width: 1850px;
      display: inline-block;
     
	}

    .controls{
	padding-left: 20px;
   height: 80px;
   margin-bottom: 10px;
   margin-top: 5px;
}

input[type="radio"] {
  -ms-transform: scale(1.5); /* IE 9 */
  -webkit-transform: scale(1.5); /* Chrome, Safari, Opera */
  transform: scale(1.5);
}

   </style>

   