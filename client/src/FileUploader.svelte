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
  let hasError = false;
  

  function handleUpdate(event) {
    isOpen = event.detail.isOpen;
  }
     let data=[];

   async function openFile(fl){
	hasError= false; 
	data = await controller.openFile(fl);
	if(data instanceof Error){
		hasError= true;
	}
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
       <img src="/images/snp-24.png" alt="DArTView logo" />
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
<p>Oops, error occured. Check you have a proper DArT Marker file and upload again </p>
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