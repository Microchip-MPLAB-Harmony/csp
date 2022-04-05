import { ProgressSpinner } from 'primereact/progressspinner';
import { useState } from 'react';

let setValuMethod : any;
export function DisaableProgress (){
    setValuMethod(false)
}
const ShowProgress = () => {
    const [value, setValue] = useState(true); 
    setValuMethod = setValue;
    return(<div>
        {value && <ProgressSpinner />}
    </div>)
}

export default ShowProgress;