<script>
   import VirtualList from './VirtualList.svelte';
    let data=[];
    let sampleNumber=0;
    let hasError=false;
    const width = window.innerWidth;
    const height = window.innerHeight;

    let start;
    let end;
    let scores;

$: loadData= async () => {
      hasError = false;
     await fetch('http://127.0.0.1:5000/upload_file')
                 .then(response => response.json())
                 .then(obj => 
                 {
                    data=obj;
                    sampleNumber= data[0].length
                    
                     console.log(data);
                  
                 })
                 .catch(error => {
                    hasError= true;
                    console.log(error);
                 })                 

}

$: sortData= async () => {
      hasError = false;
     await fetch('http://127.0.0.1:5000/sort_data')
                 .then(response => response.json())
                 .then(obj => 
                 {
                    data=obj;
                    sampleNumber= data[0].length
                    
                     console.log(data);
                  
                 })
                 .catch(error => {
                    hasError= true;
                    console.log(error);
                 })                 

}

</script>
<div>
<span><button on:click={loadData}>load data</button></span>
<span><button on:click={sortData}>sort data</button></span>
</div>
<div>
<p>Markers Number : {data.length}</p>
<p>Sample Number: {sampleNumber}</p>

</div>


{#if hasError}
Oops, error occured
{:else}
<div class='container'>
   
   <VirtualList  items= {data} bind:start bind:end let:item>
    <div class="row-data">
     {#each item as score}
      <span  class="allele{score} data">{score}</span>
      {/each}
   </div>
   
   </VirtualList>

   <p>showing {start}-{end} of {data.length} rows</p>

 

</div>
{/if}

<style>
   .container {
		border-top: 1px solid #333;
		border-bottom: 1px solid #333;
		min-height: 200px;
		height: calc(100vh - 15em);
     
	}

   .row-data{
      display: flex;
      border-bottom: 1pt solid #bebebe ;
      
      
   }
 

   .allele0{
      background-color: chartreuse;
   }

   .allele1{
      background-color: cyan;
   }

   .allele2{
      background-color: rgb(245, 41, 41);
   }

   .allele-{
      background-color: aliceblue;
   }
   .alleleid{
      display: block;
   }

   .data{
      font-family: 'Source Code Pro', monospace;
      text-align: center;
      min-height: 2px;
      min-width: 2px;
      align-items: center;
      justify-content: center;
      border-radius: 1px;
      font-size: 2px;
      display: inline-flex;


   }
   
    </style>
