import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { useContext, useEffect, useState } from 'react';
import {
    CheckBoxDefault,
    configSymbolApi,
    InputNumberDefault,
    PluginConfigContext,
    useBooleanSymbol,
    useComboSymbol,
    useIntegerSymbol,

} from '@mplab_harmony/harmony-plugin-client-lib';
import {
    getDynamicSymbolsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import LoadDynamicComponents from 'clock-common/lib/Components/Dynamic/LoadDynamicComponents';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import { InputNumber } from 'primereact/inputnumber';
import { GetClockDisplayFreqValue } from 'clock-common/lib/Tools/Tools';


const ExtClkSrcControllerBox = (props: {
    ExtClkSrcControllerData: ControlInterface[];
    cx: (...classNames: string[]) => string;
}) => {
    const { componentId = 'core' } = useContext(PluginConfigContext);

    const [dynamicSymbolInfo] = useState(() =>
        getDynamicSymbolsFromJSON(props.ExtClkSrcControllerData)
    );

    const extClkSrcFrq = useIntegerSymbol({
        componentId,
        symbolId: 'extClkSrcFreq'
    });

    const refi1Freq = useIntegerSymbol({
        componentId,
        symbolId: 'referenceInputPinFreq1'
    });

    const refi2Freq = useIntegerSymbol({
        componentId,
        symbolId: 'referenceInputPinFreq2'
    });

    const refInput1Hook = useBooleanSymbol({
        componentId,
        symbolId: "referenceInputPinEnable1"
    });

    const refInput2Hook = useBooleanSymbol({
        componentId,
        symbolId: "referenceInputPinEnable2"
    });

    const extClkSrc = useComboSymbol({
        componentId,
        symbolId: "extClkSrcSel"
    });

    const [poscFreqTooltip, setPoscFreqTooltip] = useState(extClkSrc.value);
    const [refFreqTooltip, setRefFreqTooltip] = useState(extClkSrc.value);

    useEffect(() => {
        configSymbolApi.getSymbol(componentId, `extClkSrcFreq`)
            .then((data) => setPoscFreqTooltip(`Min: ${GetClockDisplayFreqValue(data.min)}, Max: ${GetClockDisplayFreqValue(data.max)}`));
        configSymbolApi.getSymbol(componentId, 'referenceInputPinFreq1')
            .then((data) => setRefFreqTooltip(`Max: ${GetClockDisplayFreqValue(data.max)}`));
    }, [extClkSrc.value]);


    return (
        <div>
            <LoadDynamicComponents
                componentId={componentId}
                dynamicSymbolsInfo={dynamicSymbolInfo}
                cx={props.cx}
            />
            <PlainLabel
                disPlayText="Enable Clock Fail Interrupt"
                className={props.cx('clkFailIntLable')}
            />
            <CheckBoxDefault
                componentId={componentId}
                symbolId={'clockFailIntEnable'}
                className={props.cx('clkFailIntEnable')}
            />

            <PlainLabel
                disPlayText="External Clock (POSC) Source"
                className={props.cx('extClkSrcLabel')}
            />
            {/* {extClkSrc.value !== "None" && ( */}
            <PlainLabel
                disPlayText={`Primary/External Clock Frequency (POSC)`}
                className={props.cx('priClkFreqLabel')}
            />
            {/* // )} */}
            {extClkSrc.value !== "Primary Oscillator" && (
                <PlainLabel
                    disPlayText={`Enable CLKO Pin`}
                    className={props.cx('enableClkOpPin')}
                />
            )}
            <PlainLabel
                disPlayText={`Use Reference Input 1(REFI1)`}
                className={props.cx('enableRefIpPin1Label')}
            />
            {refInput1Hook.value && (
                <PlainLabel
                    disPlayText="Frequency"
                    className={props.cx('refi1FreqLabel')}
                />
            )}
            <PlainLabel
                disPlayText={`Use Reference Input 2(REFI2)`}
                className={props.cx('enableRefIpPin2Label')}
            />
            {refInput2Hook.value && (
                <PlainLabel
                    disPlayText="Frequency"
                    className={props.cx('refi2FreqLabel')}
                />
            )}
            {extClkSrc.value == "None" && (
                <InputNumber
                    value={0}
                    suffix=' Hz'
                    showButtons={false}
                    className={props.cx('primaryOscFreq')}
                    disabled={true}
                />)
            }

            <InputNumberDefault
                componentId={componentId}
                symbolId={'extClkSrcFreq'}
                tooltip={poscFreqTooltip}
                className={props.cx('primaryOscFreq')}
                showButtons={false}
                suffix=" Hz"
            />
            <InputNumberDefault
                componentId={componentId}
                symbolId={'referenceInputPinFreq1'}
                tooltip={refFreqTooltip}
                className={props.cx('refi1Freq')}
                showButtons={false}
                suffix=" Hz"
            />
            <InputNumberDefault
                componentId={componentId}
                symbolId={'referenceInputPinFreq2'}
                tooltip={refFreqTooltip}
                className={props.cx('refi2Freq')}
                showButtons={false}
                suffix=" Hz"
            />
            {/* <FrequencyLabelComponent
                componentId={componentId}
                symbolId={'POSC_OUT_FREQ'}
                tooltip='When in HS mode, POSC input frequency needs to be between 4 Mhz and 32 Mhz.'
                minMaxOutofRangeRedColorStatus={
                    (poscFreqHook.value < 4000000 || poscFreqHook.value > 32000000) && poscMod.value === 'HS'
                }
                className={props.cx('lbl_poscFreq')}
            /> */}
        </div>
    );
};



export default ExtClkSrcControllerBox;