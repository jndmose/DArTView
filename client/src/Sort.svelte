
<script>

</script>
<p>Sort Criteria</p>
<hr>
<p><b>Sort Key 1 </b></p>
<div class="sortkey">
<select class="form-select" aria-label="Default select example">
  <option selected>-undefined-</option>
  <option value="1">CallRate</option>
  <option value="2">AleleFreq</option>
  <option value="3">RepAvg</option>
</select>

<div class="radio-buttons">
<div class="form-check form-check-inline">
  <input class="form-check-input" type="radio" name="inlineRadioOption" id="inlineRadio1" value="option1" checked>
  <label class="form-check-label" for="inlineRadio1">Ascending</label>
</div>
<div class="form-check form-check-inline">
  <input class="form-check-input" type="radio" name="inlineRadioOption" id="inlineRadio2" value="option2">
  <label class="form-check-label" for="inlineRadio2">Descending</label>
</div>
</div>
</div>
<p><b>Sort Key 2 </b></p>
<div class="sortkey">
<select class="form-select" aria-label="Default select example">
  <option selected>-undefined-</option>
  <option value="1">CallRate</option>
  <option value="2">AleleFreq</option>
  <option value="3">RepAvg</option>
</select>
<div class="radio-buttons">
<div class="form-check form-check-inline">
  <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="option1" checked>
  <label class="form-check-label" for="inlineRadio1">Ascending</label>
</div>
<div class="form-check form-check-inline">
  <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" value="option2">
  <label class="form-check-label" for="inlineRadio2">Descending</label>
</div>
</div>
</div>
<hr>
<div class="submit-buttons">
<input type="submit" class="btn btn-info buttons" value="Submit">
<input type="submit" class="btn btn-info buttons" value="Reset">
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
