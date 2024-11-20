
<script>
  import Controller from './Controller.js';
  import{geno_data, modal, selected1,selected2, sort_order1, sort_order2} from './data.js';
  const controller = new Controller();
   async function handleSubmit(event) {
    event.preventDefault();
    console.log('Sort order is', sort_order1);
    $geno_data = await controller.sortData($selected1, $sort_order1);
    modal.set(null);
 
  };

  export let metadata =[];
  $: new_metadata= metadata
  
  
	
</script>
<p>Sort Criteria</p>
<hr>

<form  on:submit={handleSubmit}>
  <p><b>Sort Key 1 </b></p>

<div class="sortkey">

<select class="form-select" bind:value={$selected1}  aria-label="Default select example">
  
  <option selected>-undefined-</option>
  {#each new_metadata as mtdata}
  <option value={mtdata}>{mtdata}</option>
 {/each}
</select>

<div class="radio-buttons">
<div class="form-check form-check-inline">
  <input class="form-check-input" type="radio"  value="Ascending" bind:group={$sort_order1}>
  <label class="form-check-label" for="inlineRadio1">Ascending</label>
</div>
<div class="form-check form-check-inline">
  <input class="form-check-input" type="radio"  value="Descending" bind:group={$sort_order1}>
  <label class="form-check-label" for="inlineRadio2">Descending</label>
</div>
</div>
</div>
<p><b>Sort Key 2 </b></p> 
<div class="sortkey">
  <select class="form-select" bind:value={$selected2}  aria-label="Default select example">
  
    <option selected>-undefined-</option>
    {#each new_metadata as mtdata}
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
<input type="submit" class="btn btn-info buttons" value="Submit">
<input type="reset" class="btn btn-info buttons" value="Reset">
</div>
</form>

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
