<script>
	
	import {
    Collapse,
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink,
    Dropdown,
    DropdownToggle,
    DropdownMenu,
    DropdownItem
  } from 'sveltestrap';
	
	import VirtualList from './VirtualList.svelte';
	import DragDrop from "./DragDrop.svelte";
	import Controller from './Controller.js';


	import { Styles } from 'sveltestrap';
	
  let isOpen = false;
  
  const controller = new Controller();

  function handleUpdate(event) {
    isOpen = event.detail.isOpen;
  }
    let data=[];
    let  sampleNumber=0;
    let hasError=false;
    const width = window.innerWidth;
    const height = window.innerHeight;

    let start;
    let end;

  

   
   async function openFile(fl){ 
	data = await controller.openFile(fl);
	
	sampleNumber = data[0].length;
   }

   async function sortData() {
	data = await controller.sortData();
	
		sampleNumber= data[0].length;
	
   }

   $: runUpload =  () => {
      
	  const upload=   document.getElementById("upload");
	  
	  upload.click();
	  return false;

   }


</script>
<Styles />
<div class='dartView'>
<Navbar color="light" light expand="md">
	<NavbarBrand >
       <img src="/images/snp-24.png" alt="DArTView" />
   </NavbarBrand>
	<NavbarToggler on:click={() => (isOpen = !isOpen)} />
	<Collapse {isOpen} navbar expand="md" on:update={handleUpdate}>
	  <Nav  navbar>
		<Dropdown autoClose="inside">
			<DropdownToggle nav caret>Import</DropdownToggle>
			<DropdownMenu end>
			  <DropdownItem  on:click ={runUpload}  >Import Markers </DropdownItem>
			  <DropdownItem on:click ={runUpload}>Import Samples</DropdownItem>
			  <DropdownItem divider />
			  <DropdownItem on:click ={runUpload}>Close</DropdownItem>
			</DropdownMenu>
		  </Dropdown>
		<NavItem>
		  <NavLink href="#" on:click={runUpload}>Load</NavLink>
		</NavItem>
		<NavItem>
		  <NavLink href="https://github.com/bestguy/sveltestrap">About</NavLink>
		</NavItem>
		
	  </Nav>
	</Collapse>
  </Navbar>
<input id="upload" type="file"  on:change={openFile} value=""/>
{#if sampleNumber > 0 }
<div class="controls">
 <span> Samples : {sampleNumber}</span> &nbsp; <span>Markers : {data.length}</span> &nbsp;
 <button class="top-buttons" on:click={sortData}> Sort Data</button>
 <label for="homo">Homozygote Ref</label><br>
 <input type="color" id="favcolor" name="favcolor" value="#ff0000">
 
 </div>
 
{/if}


{#if hasError}
Oops, error occured
{:else}


<div class='container'>
   
   {#if sampleNumber > 0}
   <VirtualList  items= {data} bind:start bind:end let:item>
    <div class="row-data">
     {#each item as score}
      <span  class="allele{score} data">{score}</span>
      {/each}

      
   </div>
   
   </VirtualList>
   {/if}

   {#if sampleNumber === 0 }

   <DragDrop on:change={() => console.log("Files changed")} callback={() => alert("Thanks")}></DragDrop>
 
  
   {/if}



</div>
{/if}

</div>
{#if sampleNumber > 0}

<div class="footer"><p>Showing {start}-{end} of {data.length} Markers</p></div>
	
{/if}
<style>
	
	.container {
      width: 100%;
	  padding: 20px;
	  min-height: 200px;
	  height: calc(100vh - 15em);
      max-width: 1850px;
     
	}
   #upload{
    display:none
}
.dartView{
	border: 1px solid black;
	background: #dcdcdc;
	
}

.controls{
	padding-left: 20px;
   height: 80px;
   margin-bottom: 10px;
   margin-top: 5px;
}

img{
   max-height: 50px;
}
   .row-data{
      display: flex;
      border-bottom: 1pt solid #bebebe ;
      
      
   }
 

   .allele0{
      background-color: #3498db;
   }

   .allele1{
      background-color: #2ecc71;
   }

   .allele2{
      background-color: #e74c3c;
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

  
	.buttons {
		width: 40%;
		display: flex;
     
	}
	
</style>