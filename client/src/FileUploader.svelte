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
	import Controller from './Controller.js';
   const controller = new Controller();

   import { Styles } from 'sveltestrap';
  
  import DragDrop from './DragDrop.svelte';
  import ListDisplay from './ListDisplay.svelte';
	
	
	
  let isOpen = false;
  

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


{#if hasError}
Oops, error occured
{:else}

   {#if data.length > 0}
   <ListDisplay geno_data={data} />
   
   {:else }
   <DragDrop />
 
  
   {/if}

{/if}

</div>
<style>
	
	
   #upload{
    display:none
}
.dartView{
	border: 1px solid black;
	background: #dcdcdc;
	height: -webkit-fill-available;
	
}


img{
   max-height: 50px;
}
  


  
   
	
</style>