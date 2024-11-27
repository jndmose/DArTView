import { writable } from 'svelte/store';

export let modal = writable(null);
export let geno_data = writable([]);
export let selected1= writable('-unsorted-');
export let sort_order1=writable('Ascending');
export let selected2= writable('-unsorted-');
export let sort_order2=writable('Ascending');
export let selected3= writable('-unsorted-');
export let sort_order3=writable('Ascending');
export let cssVarStyles = writable([]);
