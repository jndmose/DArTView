import { onDestroy } from 'svelte';
import Spinner from '../components/Spinner.svelte';
let spinner_text = "Loading..."

export const loader = (node, loading) => {

	if(node.className === "sort-spinner"){
		spinner_text= "Sorting data..."
	}
	else if(node.className==="upload-spinner"){
		spinner_text= "Loading data..."
	}
	
	let Spin, loadingValue;
	const unsubscribe = loading.subscribe(loading => {
		if(loading){
			
			Spin = new Spinner({
				target: node,
				intro: true,
				props: {spinner_text}
			})
		} else {
			if(Spin){
				Spin?.$destroy?.()
				Spin = undefined;
			}
		}
	})
	onDestroy(unsubscribe);
	
}