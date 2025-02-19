import { useState } from 'react';
import {
    componentUtilApi,
    configSymbolApi
} from '@mplab_harmony/harmony-plugin-client-lib';
import { Button } from 'primereact/button';
import { InputNumber } from 'primereact/inputnumber';
import { GetClockDisplayFreqValue } from 'clock-common/lib/Tools/Tools';



const ClockGenAutoCalc = (props: {
    index: string
    componentId: string
    inputClkSrcFreq: number
    reqClkSrcFreq: number
    maxClkGenFreq: number
    close: () => void;
}) => {

    const componentId = props.componentId;


    const [reqClkGenFreq, setReqClkGenFreq] = useState(props.reqClkSrcFreq);
    const [clkGenOutputValue, setClkGenOutputValue] = useState(props.reqClkSrcFreq);

    interface ClkGenParamsMap {
        [key: string]: string | number;
    }
    const [clkGenParamsMap, setClkGenParamsMap] = useState<ClkGenParamsMap>({});

    interface CalcMap {
        calcClkGenFreq?: number;
        [key: string]: any;
    }

    const updateClkGenParams = (calcMap: CalcMap) => {
        if (calcMap.calcClkGenFreq !== undefined) {
            setClkGenOutputValue(calcMap.calcClkGenFreq);
            delete calcMap.calcClkGenFreq;
        }
        setClkGenParamsMap(calcMap);
    };

    const handleClick = async () => {
        const message = "CONFIGURATOR_CLOCK_AUTO_CALCULATE_CLK_GEN_DIVIDERS";
        let requestMap: any = {};
        requestMap["clkGenNo"] = props.index;
        requestMap["requestedClkGenFreq"] = reqClkGenFreq;
        componentUtilApi.sendMessage(componentId, message, requestMap).then((clkGenParams) => {
            updateClkGenParams(clkGenParams);
        });
    };

    const accept = () => {
        for (const key in clkGenParamsMap) {
            if (clkGenParamsMap.hasOwnProperty(key)) {
                const value = clkGenParamsMap[key];
                configSymbolApi.setValue(props.componentId, key, value);
            }
        }
        props.close();
    };
    const cancel = () => {
        props.close();
    };

    const maxFreqLabel = 'Hz <='+ GetClockDisplayFreqValue(props.maxClkGenFreq)
    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: '1.5rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                <label>
                    Clock Source Frequency :
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
                    Requested Clock Generator Output frequency:
                </label>
                { (
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                        <InputNumber
                            value={reqClkGenFreq}
                            onValueChange={(e) => setReqClkGenFreq(e.value !== null ? e.value : 0)}
                            placeholder="Enter Frequency(Hz)"
                            showButtons={false}
                            max={props.maxClkGenFreq}
                        />
                        <label>
                        {maxFreqLabel}
                        </label>
                    </div>

                )}
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                <Button
                    label={'Calculate'}
                    onClick={handleClick}
                />
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                <label>
                    Calculated Clock Generator Output frequency:
                </label>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <InputNumber
                        value={clkGenOutputValue}
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
                />
                <Button
                    label={'Cancel'}
                    onClick={cancel}
                />
            </div>
        </div>
    );
};

export default ClockGenAutoCalc;