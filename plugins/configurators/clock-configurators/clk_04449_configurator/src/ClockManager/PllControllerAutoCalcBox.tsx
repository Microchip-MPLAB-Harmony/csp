import { useState } from 'react';
import {
    componentUtilApi,
    configSymbolApi
} from '@mplab_harmony/harmony-plugin-client-lib';
import { Button } from 'primereact/button';
import { InputNumber } from 'primereact/inputnumber';
import { InputTextarea } from 'primereact/inputtextarea';


const PLLControllerAutoCalcBox = (props: {
    index: string
    componentId: string
    inputClkSrcFreq: number
    initialPlloFreq: number
    initialPllVcoFreq: number
    close: () => void;
}) => {

    const componentId = props.componentId;
    const maxPllVcoFreq = 800000000;
    const maxPlloFreq = 800000000;

    const [isChecked1, setIsChecked1] = useState(false);
    const [isChecked2, setIsChecked2] = useState(false);
    const [inputValue1, setInputValue1] = useState(props.initialPlloFreq);
    const [inputValue2, setInputValue2] = useState(props.initialPllVcoFreq);
    const [plloOutputValue, setPlloOutputValue] = useState(props.initialPlloFreq);
    const [plloVcoDivValue, setPlloVcoDivValue] = useState(props.initialPllVcoFreq);

    interface PllParamsMap {
        [key: string]: string | number;
    }
    const [pllParamsMap, setPllParamsMap] = useState<PllParamsMap>({});

    interface CalcMap {
        calcPlloFreq?: number;
        calcPllVcoDivFreq?: number;
        [key: string]: any;
    }

    const updatePllParams = (calcMap: CalcMap) => {
        if (calcMap.calcPlloFreq !== undefined) {
            setPlloOutputValue(calcMap.calcPlloFreq);
            delete calcMap.calcPlloFreq;
        }
        if (calcMap.calcPllVcoDivFreq !== undefined) {
            setPlloVcoDivValue(calcMap.calcPllVcoDivFreq);
            delete calcMap.calcPllVcoDivFreq;
        }
        setPllParamsMap(calcMap);
    };

    const handleClick = async () => {
        const message = "CONFIGURATOR_CLOCK_AUTO_CALCULATE_PLL_DIVIDERS";
        let requestMap: any = {};
        requestMap["pllNo"] = props.index;
        requestMap["pllClkSrcFreq"] = props.inputClkSrcFreq;
        if (isChecked1) {
            requestMap["reqPlloFreq"] = inputValue1;
        }
        if (isChecked2) {
            requestMap["reqPllVcoDivFreq"] = inputValue2;
        }
        componentUtilApi.sendMessage(componentId, message, requestMap).then((pllParams) => {
            updatePllParams(pllParams);
        });
    };

    const handleCheckbox1Change = (event: React.ChangeEvent<HTMLInputElement>) => {
        setIsChecked1(event.target.checked);
    };

    const handleCheckbox2Change = (event: React.ChangeEvent<HTMLInputElement>) => {
        setIsChecked2(event.target.checked);
    };

    const accept = () => {
        for (const key in pllParamsMap) {
            if (pllParamsMap.hasOwnProperty(key)) {
                const value = pllParamsMap[key];
                configSymbolApi.setValue(props.componentId, key, value);
            }
        }
        props.close();
    };
    const cancel = () => {
        props.close();
    };


    return (


        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: '1.5rem' }}>
            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '1.5rem' }}>
                <InputTextarea
                    value={"Note: The PLL FOUT frequency and PLL VCO DIV frequency share the same PLLPRE divider and FBDIV multiplier components. If only the PLL FOUT frequency is requested, the PLL VCO DIV frequency will also be updated accordingly, and vice versa.\nIf both frequencies are requested simultaneously, the auto-calculation function will aim to achieve the closest possible values for both, prioritizing the PLL FOUT frequency."}
                    rows={6} cols={90}
                />
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                <label>
                    PLL{props.index} Clock Source Frequency :
                </label>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <InputNumber
                        value={props.inputClkSrcFreq}
                        readOnly={true}
                    />
                    <label>
                        Hz
                    </label>
                </div>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                <label>
                    Request PLL{props.index} FOUT frequency
                    <input
                        type="checkbox"
                        checked={isChecked1}
                        onChange={handleCheckbox1Change}
                    />
                </label>
                {isChecked1 && (
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                        <InputNumber
                            value={inputValue1}
                            onValueChange={(e) => setInputValue1(e.value !== null ? e.value : 0)}
                            placeholder="Enter Frequency(Hz)"
                            showButtons={false}
                            max={maxPlloFreq}
                        />
                        <label>
                        {'Hz <=800 MHz'}
                        </label>
                    </div>

                )}
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                <label>
                    Request PLL{props.index} VCO DIV frequency
                    <input
                        type="checkbox"
                        checked={isChecked2}
                        onChange={handleCheckbox2Change}
                    />
                </label>
                {isChecked2 && (
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                        <InputNumber
                            value={inputValue2}
                            onValueChange={(e) => setInputValue2(e.value !== null ? e.value : 0)}
                            placeholder="Enter Frequency(Hz)"
                            showButtons={false}
                            max={maxPllVcoFreq}
                        />
                        <label>
                        {'Hz <=800 MHz'}
                        </label>
                    </div>
                )}
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                <Button
                    label={'Calculate'}
                    onClick={handleClick}
                    disabled={!isChecked1 && !isChecked2}
                />
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                <label>
                    Calculated PLL{props.index} FOUT frequency
                </label>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <InputNumber
                        value={plloOutputValue}
                        readOnly={true}
                    />
                    <label>
                        Hz
                    </label>
                </div>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                <label>
                    Calculated PLL{props.index} VCO DIV frequency (Hz)
                </label>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <InputNumber
                        value={plloVcoDivValue}
                        readOnly={true}
                    />
                    <label>
                        Hz
                    </label>
                </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '1.5rem' }}>
                <Button
                    label={'Accept'}
                    onClick={accept}
                    disabled={!isChecked1 && !isChecked2}
                />
                <Button
                    label={'Cancel'}
                    onClick={cancel}
                />
            </div>
        </div>
    );
};

export default PLLControllerAutoCalcBox;