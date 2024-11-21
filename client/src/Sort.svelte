
<script>
  import Controller from './Controller.js';
  import{geno_data, modal, selected1,selected2, sort_order1, sort_order2,selected3,sort_order3} from './data.js';
  import {createEventDispatcher} from 'svelte';
  const controller = new Controller();
   async function handleSelected(event) {
    $geno_data = await controller.sortData($selected1, $sort_order1,$selected2,$sort_order2,$selected3, $sort_order3);
 
  };
  export let metadata =[];


 function handleExit(){

  modal.set(null);

 }
  
  
  
	
</script>
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
  <select class="form-select" bind:value={$selected2}  aria-label="Default select example">
  
    <option selected>-unsorted-</option>
    {#each metadata as mtdata}
    <option value={mtdata}>{mtdata}</option>
   {/each}
  </select>
  
  <div class="radio-buttons">
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio"  value="Ascending" bind:group={$sort_order2}>
      <label class="form-check-label" for="inlineRadio1">Ascending</label>
    </div>
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio"  value="Descending" bind:group={$sort_order2}>
      <label class="form-check-label" for="inlineRadio2">Descending</label>
    </div>
    </div>
 </div>

 <p><b>Sort Key 2 </b></p> 
<div class="sortkey">
  <select class="form-select" bind:value={$selected2}  aria-label="Default select example">
  
    <option selected>-unsorted-</option>
    {#each metadata as mtdata}
    <option value={mtdata}>{mtdata}</option>
   {/each}
  </select>
  
  <div class="radio-buttons">
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio"  value="Ascending" bind:group={$sort_order2}>
      <label class="form-check-label" for="inlineRadio1">Ascending</label>
    </div>
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio"  value="Descending" bind:group={$sort_order2}>
      <label class="form-check-label" for="inlineRadio2">Descending</label>
    </div>
    </div>
 </div>
<hr>
<div class="submit-buttons">

<input type="button" class="btn btn-info buttons" value="Exit" on:click={handleExit}>
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
