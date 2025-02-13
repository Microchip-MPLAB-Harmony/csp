import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import { useContext, useState } from 'react';
import {
    CheckBoxDefault,
    ComboBoxDefault,
    configSymbolApi,
    KeyValueSetRadio,
    PluginConfigContext,
    useBooleanSymbol,
    useIntegerSymbol,
    useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import {
    getDynamicLabelsFromJSON,
    getDynamicSymbolsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';
import { Dialog } from 'primereact/dialog';
import PLLControllerAutoCalcBox from './PllControllerAutoCalcBox';
import { ControlInputNoInterface, GetButton, LoadDynamicInputNoComponents } from './ClockHelper/LoadDynamicInputNoComponents';
import { GetClockDisplayFreqValue } from 'clock-common/lib/Tools/Tools';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';

const PLLControllerBox = (props: {
    index: string
    PLLControllerData: ControlInterface[];
    cx: (...classNames: string[]) => string;
}) => {
    const { componentId = 'core' } = useContext(PluginConfigContext);

    const pllEnable = useBooleanSymbol({
        componentId,
        symbolId: 'pll' + props.index + 'Enable'
    });

    const pllClkSrcFreq = useIntegerSymbol({
        componentId,
        symbolId: 'pll' + props.index + 'ClockSourceFreq'
    });

    const pllPfdFreq = useIntegerSymbol({
        componentId,
        symbolId: 'pll' + props.index + 'calculatedPfdFrequency'
    });

    const pllCalcPlloFreq = useIntegerSymbol({
        componentId,
        symbolId: 'pll' + props.index + 'calculatedFoutFrequency'
    });
    const pllCalcVcoDivFreq = useIntegerSymbol({
        componentId,
        symbolId: 'pll' + props.index + 'calculatedVCOFrequency'
    });

    const [dialogStatus, setdialogStatus] = useState(false);

    function pllAutoCalculationButtonClicked() {
        setdialogStatus(true);
    }

    const dialogClosed = (acceptStatus: boolean) => {
        setdialogStatus(false);
    };

    const [dynamicSymbolInfo] = useState(() => {
        let inputNoFields: ControlInputNoInterface[] = getDynamicSymbolsFromJSON(props.PLLControllerData);
        inputNoFields.forEach((e) => {
            configSymbolApi.getSymbol(componentId, e.symbol_id ?? "").then((data) => e.tooltip = `Min: ${data.min}, Max: ${data.max}`)
        })
        return inputNoFields;
    }
    );

    const [dynamicLabelSymbolsInfo] = useState(() => getDynamicLabelsFromJSON(props.PLLControllerData));

    const clockSource = useKeyValueSetSymbol({
        componentId,
        symbolId: 'pll' + props.index + 'CON__NOSC'
    });

    let pllSymbols = [
        'pll' + props.index + 'EnableFailSafeClockPll',
        'pll' + props.index + 'CON__BOSC'
    ];

    let pllResetSymbols = [
        'pll' + props.index + 'CON__NOSC',
        'pll' + props.index + 'DIV__PLLPRE',
        'pll' + props.index + 'DIV__PLLFBDIV',
        'pll' + props.index + 'DIV__POSTDIV1',
        'pll' + props.index + 'DIV__POSTDIV2',
        'vco' + props.index + 'DIV__INTDIV',
        'pll' + props.index + 'EnableFailSafeClockPll',
        'pll' + props.index + 'CON__BOSC'
    ];

    const minPllPfdFreq = 500000000;
    const maxPllPfdFreq = 1600000000;
    const maxPlloFreq = 800000000;
    const maxPllVcoFreq = 800000000;

    const textColorPllPfdFreq = pllEnable.value && (pllPfdFreq.value > maxPllPfdFreq || pllPfdFreq.value < minPllPfdFreq)? "Red" :"Black" ;
    const textColorPllOutFreq = pllEnable.value && pllCalcPlloFreq.value > maxPlloFreq ? "Red" :"Black" ;
    const textColorPllVcoFreq = pllEnable.value && pllCalcVcoDivFreq.value > maxPllVcoFreq ? "Red" :"Black" ;
    return (
        <div>
            <SettingsDialog
                tooltip={'Phase Lock Loop ' + props.index + ' Advanced Settings'}
                componentId={componentId}
                className={props.cx('pll' + props.index + 'Clk_Settings')}
                symbolArray={pllSymbols}
                dialogWidth='50rem'
                dialogHeight='40rem'
                disabled={!pllEnable.value}
            />
            <CheckBoxDefault
                componentId={componentId}
                symbolId={'pll' + props.index + 'Enable'}
                className={props.cx('pll' + props.index + '_enable')}
            />
            <ComboBoxDefault
                componentId={componentId}
                symbolId={'pll' + props.index + 'DIV__POSTDIV1'}
                className={props.cx('pll' + props.index + 'Postdiv1')}
                disabled={!pllEnable.value}
            />
            <ComboBoxDefault
                componentId={componentId}
                symbolId={'pll' + props.index + 'DIV__POSTDIV2'}
                className={props.cx('pll' + props.index + 'Postdiv2')}
                disabled={!pllEnable.value}
            />
            <LoadDynamicInputNoComponents
                componentId={componentId}
                dynamicSymbolsInfo={dynamicSymbolInfo}
                cx={props.cx}
                disable={!pllEnable.value}
            />
            <LoadDynamicFreqencyLabels
                componentId={componentId}
                dynamicLabelSymbolsInfo={dynamicLabelSymbolsInfo}
                cx={props.cx}
            />
            <KeyValueSetRadio
                keyValueSetSymbolHook={clockSource}
                classPrefix={'pll' + props.index + 'ClkRadio'}
                labelClassPrefix={'pll' + props.index + 'ClkRadioName'}
                classResolver={props.cx}
                disabled={!pllEnable.value}
            />
            <PlainLabel
                disPlayText={GetClockDisplayFreqValue(pllPfdFreq.value)}
                className={props.cx('pll' + props.index +'FvcoFreq')}
                toolTip={"Min: 500 MHz, Max: 1600 MHz"}
                redColorStatus = {textColorPllPfdFreq == "Red" ? true:false}
            />
            <PlainLabel
                disPlayText={GetClockDisplayFreqValue(pllCalcPlloFreq.value)}
                className={props.cx('pll' + props.index +'_plloFreq')}
                toolTip={"Max: 800 MHz"}
                redColorStatus = {textColorPllOutFreq == "Red" ? true:false}
            />
            <PlainLabel
                disPlayText={GetClockDisplayFreqValue(pllCalcVcoDivFreq.value)}
                className={props.cx('pll' + props.index +'_pllVcoFreq')}
                toolTip={"Max: 800 MHz"}
                redColorStatus = {textColorPllVcoFreq == "Red" ? true:false}
            />
            <ResetSymbolsIcon
                tooltip={'Reset Phase Lock Loop ' + props.index + ' Settings to default value'}
                className={props.cx('pll' + props.index + 'Clk_reset')}
                componentId={componentId}
                resetSymbolsArray={pllResetSymbols}
                disabled={!pllEnable.value}
            />
            <GetButton
                buttonDisplayText={'Auto Calculate...'}
                className={props.cx('pll' + props.index + 'AutoCalc')}
                toolTip={'click here for PLL Auto Calculation'}
                buttonClick={pllAutoCalculationButtonClicked}
                disabled={!pllEnable.value}
            />
            <Dialog
                header='Auto Calculate PLL FOUT and PLL VCO DIV frequencies'
                visible={dialogStatus}
                maximizable={true}
                style={{ width: '55rem', height: '45rem' }}
                onHide={() => {
                    dialogClosed(false);
                }}>
                <PLLControllerAutoCalcBox
                    index={props.index}
                    componentId={componentId}
                    inputClkSrcFreq={pllClkSrcFreq.value}
                    initialPlloFreq={pllCalcPlloFreq.value}
                    initialPllVcoFreq={pllCalcVcoDivFreq.value}
                    close={() => {
                        dialogClosed(false);
                    }}
                />
            </Dialog>
        </div>
    );
};

export default PLLControllerBox;