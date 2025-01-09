
<script>
  import Controller from './Controller.js';
  import{geno_data, modal, selected1,selected2, sort_order1, sort_order2,selected3,sort_order3} from './data.js';
  import {createEventDispatcher} from 'svelte';
  import { loader } from './loader';
  import { writable  }from 'svelte/store';
  
  const controller = new Controller();
   async function handleSelected(event) {
    runUpdate(true);
  
    $geno_data = await controller.sortData($selected1, $sort_order1,$selected2,$sort_order2,$selected3, $sort_order3);
    runUpdate(false);
 
  };
  export let metadata =[];



 function handleExit(){

  modal.set(null);

 }

 
	let loading = writable(false);
	
	function runUpdate(val) {
		loading.update(n => n=val);
  
  }
  
	
</script>
<div class="sort-spinner" use:loader={loading}>
<ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link active" aria-current="page" href="#marker-tab" data-toggle='tab' >Marker Metadata</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#sample-tab" data-toggle='tab'>Sample Metadata</a>
  </li>

</ul>

<div class="tab-content">

<div class='tab-pane container fade in show active' id="marker-tab">

<p>Sort Criteria</p>
<hr>
  <p><b>Sort Key 1 </b></p>

<div class="sortkey">

<select class="form-select" bind:value={$selected1}  aria-label="Metadata Select" on:change={handleSelected}>
  
  <option selected>-unsorted-</option>
  {#each metadata as mtdata}
  <option value={mtdata}>{mtdata}</option>
 {/each}
</select>

<div class="radio-buttons">
<div class="form-check form-check-inline">
  <input class="form-check-input" type="radio"  value="Ascending" bind:group={$sort_order1} on:change={handleSelected}>
  <label class="form-check-label" for="inlineRadio1">Ascending</label>
</div>
<div class="form-check form-check-inline">
  <input class="form-check-input" type="radio"  value="Descending" bind:group={$sort_order1} on:change={handleSelected}>
  <label class="form-check-label" for="inlineRadio2">Descending</label>
</div>
</div>
</div>
<p><b>Sort Key 2 </b></p> 
<div class="sortkey">
  <select class="form-select" bind:value={$selected2}  aria-label="Metadata Select" on:change={handleSelected}>
  
    <option selected>-unsorted-</option>
    {#each metadata as mtdata}
    <option value={mtdata}>{mtdata}</option>
   {/each}
  </select>
  
  <div class="radio-buttons">
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio"  value="Ascending" bind:group={$sort_order2} on:change={handleSelected}>
      <label class="form-check-label" for="inlineRadio1">Ascending</label>
    </div>
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio"  value="Descending" bind:group={$sort_order2} on:change={handleSelected}>
      <label class="form-check-label" for="inlineRadio2">Descending</label>
    </div>
    </div>
 </div>

 <p><b>Sort Key 3 </b></p> 
<div class="sortkey">
  <select class="form-select" bind:value={$selected3} aria-label="Metadata Select" on:change={handleSelected}>
  
    <option selected>-unsorted-</option>
    {#each metadata as mtdata}
    <option value={mtdata}>{mtdata}</option>
   {/each}
  </select>
  
  <div class="radio-buttons">
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio"  value="Ascending" bind:group={$sort_order3} on:change={handleSelected}>
      <label class="form-check-label" for="inlineRadio1">Ascending</label>
    </div>
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio"  value="Descending" bind:group={$sort_order3} on:change={handleSelected}>
      <label class="form-check-label" for="inlineRadio2">Descending</label>
    </div>
    </div>
 </div>
<hr>
<div class="submit-buttons">

<input type="button" class="btn btn-info buttons" value="Exit" on:click={handleExit}>
</div>
</div>
<div class='tab-pane container fade' id="sample-tab">

  <p>Samples Panel</p>
</div>

</div>

</div>

<style>
  .sortkey{
    display: flex;
    gap: 5px;

  }
  .radio-buttons{
    display: block;
  }
  .submit-buttons {
    margin: 30px auto;
    text-align: right;
    width: 50%;
    
}
.buttons{
  margin-left:10px;
}
</style>
