<script>
import VirtualList from './VirtualList.svelte';
import Modal, { bind } from 'svelte-simple-modal';
import Sort from './Sort.svelte';
import {geno_data, modal} from './data.js';
import { onMount } from "svelte";

let start;
let end;
let checkedX= false;
let checkedY = false;
let canvas;
let canvas_element;
const max_height= '10000';

let styles = {
		'allele2': '#e74c3c',
		'allele1': '#2ecc71',
		'allele0': '#3498db',
      'allele-': '#f0f8ff'
	};

   $: cssVarStyles = Object.entries(styles)
		.map(([key, value]) => `--${key}:${value}`)
		.join(';');


     

     let mtdata = ["MarkerCallRate", "SampleCallRate","OneRatioSnp","FreqHomRef","FreqHomSnp","FreqHets","PICRef"]

  
  const sortData = () => modal.set(bind(Sort, {metadata:mtdata}));

  const handleClickZoom = ((which) => {
   if(which=='zoomX'){
      checkedX=!checkedX;
      handleZoomXaxis();
   }
   else{
      checkedY=!checkedY;
      handleZoomYaxis();
   }
   
   
  })

const handleZoomXaxis = (() => {
   handleDisplayNone();

})

const handleZoomYaxis = (() => {
   handleDisplayNone();
   
})

const handleDisplayNone = (() => {
   if(!checkedX || !checkedY){
      canvas_element.style.display='none';
   }

})

const markers = $geno_data.length;

const samples = $geno_data[0].length;

//width changes when zoom x is pressed
const height=markers*2;

const handleLongHeight = (() => {
   if(height > max_height){

   }
})





onMount(() => {
   
 canvas = document.getElementById("canvas");
 canvas_element = document.getElementById("zoom-div");

});


       $: if(checkedX & checkedY){
         console.log("both checked");
         let width =  samples * 2;
         canvas.width= width;
         canvas.height= height;

         if(canvas_element !=null){

         canvas_element.style.display='block';
         }

        if (canvas.getContext) {
          const ctx = canvas.getContext("2d");
         
          for( let j =0 ; j< markers;j++){
            for(let i=0; i< samples; i++){
              
            
            if($geno_data[j][i]==="0"){
              
               ctx.fillStyle= styles['allele0'];
        
            }
            else if($geno_data[j][i]==="1"){
            ctx.fillStyle=styles['allele1']

            }
            else if($geno_data[j][i]==="2"){
             ctx.fillStyle= styles['allele2']

            }

            else {
               ctx.fillStyle= styles['allele-']

            }

            ctx.fillRect(i*2, j*2, 2, 2);

          }
        }

        }
        console.log("done");
      }

      $: if( checkedY & !checkedX){
         
         let width =  samples * 20;
         canvas.width= width;
         canvas.height= height;

         if(canvas_element !=null){

         canvas_element.style.display='block';
         }

        if (canvas.getContext) {
          const ctx = canvas.getContext("2d");
         
          for( let j =0 ; j< markers;j++){
            for(let i=0; i< samples; i++){
              
            
            if($geno_data[j][i]==="0"){
              
               ctx.fillStyle= styles['allele0'];
        
            }
            else if($geno_data[j][i]==="1"){
            ctx.fillStyle=styles['allele1']

            }
            else if($geno_data[j][i]==="2"){
             ctx.fillStyle= styles['allele2']

            }

            else {
               ctx.fillStyle= styles['allele-']

            }

            ctx.fillRect(i*20, j*2, 20, 2);

          }
        }

        }
        console.log("one done");
      }
   
   
</script>
<div id='geno-map'  style="{cssVarStyles}">

<div class="controls">
	<span> Samples : {$geno_data[0].length}</span> &nbsp; <span>Markers : {$geno_data.length}</span> &nbsp;
	<!-- <button class="top-buttons" on:click={sortData} > Sort Data</button> -->
   <Modal show={$modal}>
      <button  on:click={sortData}>Sort Data</button>
    </Modal>

    <div class="btn-group">
      <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
        Color Scheme
      </button>
      <ul class="dropdown-menu">
         <label>
            <input  style="padding:0" type="color" bind:value={styles['allele2']} />
            Hets
          </label>
          
          <label>
            <input  style="padding:0" type="color" bind:value={styles['allele0']} /> 
            Hom0
          </label>
          
            <label>
            <input  style="padding:0" type="color" bind:value={styles['allele1']} /> 
              Hom1
            </label>
          
            <label>
              <input style="padding:0" type="color" bind:value={styles['allele-']} /> 
                Missing
              </label>
       
               
       
      </ul>
    </div>

        <button style="position:relative; padding-left:26px;" on:click={ () => handleClickZoom('zoomX')}>
         <input type="checkbox" bind:checked={checkedX} style="position: absolute; top:10px; left: 4px;"> Zoom X-axis
        </button>

        <button style="position:relative; padding-left:26px;" on:click={() => handleClickZoom('zoomY')}>
         <input type="checkbox" bind:checked={checkedY} style="position: absolute; top:10px; left: 4px;"> Zoom Y-axis
        </button>

        

        
        
       
	</div>

  
<!-- {#if checkedY & checkedX} -->

<div id="zoom-div" style="display: none;" >
   <canvas id="canvas"></canvas>
</div>

    <!-- <Zoom cssVarStyles= {cssVarStyles} /> -->

    {#if checkedX & !checkedY}
    <VirtualList  items= {$geno_data} bind:start bind:end let:item>
      <div class="row-data" style="border-bottom: none;">
       {#each item as score}
        <span  class="allele{score} data" style="min-width:2px;"></span>
        {/each}
  
        
     </div>
     
     </VirtualList>
     <div class="footer"><p>Showing {start}-{end} of {$geno_data.length} Markers</p></div>
     {/if}
     
{#if !checkedX & !checkedY }
<VirtualList  items= {$geno_data} bind:start bind:end let:item>
    <div class="row-data">
     {#each item as score}
      <span  class="allele{score} data">{score}</span>
      {/each}

      
   </div>
   
   </VirtualList>
   
   <div class="footer"><p>Showing {start}-{end} of {$geno_data.length} Markers</p></div>
   {/if}
   
    </div>

   
   

   <style>

.row-data{
      display: flex;
      border-bottom: 1pt solid #bebebe ;
      
      
   }

   .btn-group{
      margin: 6px;
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
      align-items: center;
      justify-content: center;
      min-width: 20px;
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
	  padding-left: 40px;
     padding-right: 20px;
     padding-top: 20px;
     padding-bottom: 20px;
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
#zoom-div{
	  padding: 20px;
	  height: calc(105vh - 15em);
      overflow-y: scroll;
}

   </style>

   