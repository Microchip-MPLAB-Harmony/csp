import { Accordion, AccordionTab } from "primereact/accordion";
import { createClassResolver } from "@mplab_harmony/harmony-plugin-client-lib";
import CommonADCSummary from "./CommonADCSummary";
import { useSummaryData } from "./useSummaryData";
import style from "./summary.module.css";
import ADCModuleSummary from "./ADCModuleSummary";
import ChannelConfigSummary from "./ChannelConfigSummary";
const cx = createClassResolver(style);
type Props = {
  summaryData: SummaryDataProps[];
};

export type SummaryDataProps = {
  accordionHeader: string;
  summaryDetails: FieldsetDetails[] | Symbols[];
};
export type FieldsetDetails = {
  fieldSetHeader: string;
  symbols: Symbols[];
};
export type Symbols = {
  label: string;
  value: string | number | boolean;
};

const Summary = () => {
  const { summaryData } = useSummaryData();
  const AccordTab = (summary: SummaryDataProps) => {
    if (summary.accordionHeader === "General ADC Config") {
      return (
        <CommonADCSummary
          fieldsetDetails={summary.summaryDetails as FieldsetDetails[]}
        />
      );
    } else if (summary.accordionHeader === "Channel Configuration") {
      return <ChannelConfigSummary/>;
    } else
      return (
        <ADCModuleSummary accordionHeader={summary.accordionHeader}/>
      );
  };
  return (
    <div>
      <Accordion activeIndex={0} style={{ width: "80vw" }}>
        {summaryData.map((summary: SummaryDataProps) => {
          return (
            <AccordionTab
              key={summary.accordionHeader}
              header={summary.accordionHeader}
            >
              {AccordTab(summary)}
            </AccordionTab>
          );
        })}
      </Accordion>
    </div>
  );
};
export default Summary;
