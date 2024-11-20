import { writable } from 'svelte/store';

export let modal = writable(null);
export let geno_data = writable([]);
export let selected1= writable('-undefined-');
export let sort_order1=writable('Ascending');
export let selected2= writable('-undefined-');
export let sort_order2=writable('Ascending');
export let selected3= writable('-undefined-');
export let sort_order3=writable('Ascending');