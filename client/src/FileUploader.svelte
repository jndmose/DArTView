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
  
	import { loader } from './loader';
  import { writable  }from 'svelte/store';
	let loading = writable(false);
  let loading_value= "Loading data..."
	
	function runUpdate(val) {
		loading.update(n => n=val);
	}
	import Controller from './Controller.js';
  import {geno_data,sample_list,marker_list, marker_metadata, allele_ids} from './data.js';
   const controller = new Controller();

   import { Styles } from 'sveltestrap';
  
  import DragDrop from './DragDrop.svelte';
  import ListDisplay from './ListDisplay.svelte';
	
  let isOpen = false;
  let hasError = false;
  let isLoading = true;
  

  function handleUpdate(event) {
    isOpen = event.detail.isOpen;
  }
     

  async function loadFile(fl){
  runUpdate(true);
	hasError= false; 
	$geno_data = await controller.openFile(fl);
  
	if($geno_data instanceof Error){
    runUpdate(false);
		hasError= true;
	}
  else{
    runUpdate(false);
    $allele_ids= $geno_data.pop();
    $marker_metadata= $geno_data.pop();
    $sample_list = $geno_data.pop();
    $marker_list= $geno_data.pop();


  }


   }

   $: runUpload =  () => {
      
	  const upload=   document.getElementById("upload");
	  
	  upload.click();
	  return false;

   }

   
</script>
<Styles />
<div class='dartView' >
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
			  <DropdownItem  on:click ={runUpload}>Import Marker Report </DropdownItem>
			  <DropdownItem divider />
			  <DropdownItem on:click ={runUpload}>Close graphs</DropdownItem>
			</DropdownMenu>
		  </Dropdown>
      <Dropdown autoClose="inside">
        <DropdownToggle nav caret>Additional Data</DropdownToggle>
        <DropdownMenu end>
          <DropdownItem  on:click ={runUpload}>Additional Marker Metadata </DropdownItem>
          <DropdownItem divider />
          <DropdownItem on:click ={runUpload}>Additional Sample Metadata</DropdownItem>
        </DropdownMenu>
        </Dropdown>

        <Dropdown autoClose="inside">
          <DropdownToggle nav caret>BrAPI</DropdownToggle>
          <DropdownMenu end>
            <DropdownItem  on:click ={runUpload}>Authenticate BrAPI Server </DropdownItem>
            <DropdownItem divider />
            <DropdownItem on:click ={runUpload}>Load Via BrAPI_v2 server</DropdownItem>
          </DropdownMenu>
          </Dropdown>
		<NavItem>
		  <NavLink href="https://www.kddart.org/help/kdxplore/html/KDXplore-DartView-overview.html" target="_blank">About</NavLink>
		</NavItem>
		
	  </Nav>
	</Collapse>
  </Navbar>
<input id="upload" type="file"  on:change={loadFile} value=""/>

<div class="upload-spinner" use:loader={loading}>
	
{#if hasError}
<p>Oops, error occured. Check you have a proper DArT Marker file and upload again </p>
{:else}

   {#if $geno_data.length > 0}
   <ListDisplay />
   
   {:else }
   <DragDrop />
 
  
   {/if}

{/if}

</div>
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