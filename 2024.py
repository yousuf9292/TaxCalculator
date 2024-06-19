import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

st.title('Tax Calculator-2024')

st.image('https://github.com/yousuf9292/TaxCalculator/blob/main/tax.PNG')

annual_taxable_amount=st.number_input(label="Annual Taxable Amount",placeholder='Enter Taxable Amount')
calculation=st.button("Calculation")

def identifying_slab_24():
    if calculation:
        if annual_taxable_amount<=600000:
            st.text("No Tax")
        elif annual_taxable_amount>600000 and annual_taxable_amount<=1200000:
            st.text("Tax % As Per Slab: 2.5%")
            taxperappinc=annual_taxable_amount-600000
            #st.text("Tax %age Applied Income: "+str(taxperappinc))
            tax_as_per_slab=round((taxperappinc*2.5)/100)
            st.text("Tax As Per Slab: " + str(tax_as_per_slab))
            fixed_tax=0
            total_yearly_tax=tax_as_per_slab+fixed_tax
            st.markdown(f'<p style=color:green>Annual Income Tax: {str(total_yearly_tax)}</p>',unsafe_allow_html=True)
            monthly_tax=round(total_yearly_tax/12)
            st.markdown(f"<p style=color:green>Monthly Income Tax: {str(monthly_tax)}</p>",unsafe_allow_html=True)
            tax_paid_this_year=round((total_yearly_tax/annual_taxable_amount)*100,4)
            st.markdown(f"<p style=color:green>Income Tax Ratio: {str(tax_paid_this_year)}%</p>",unsafe_allow_html=True)
        elif annual_taxable_amount>1200000 and annual_taxable_amount<=2400000:
            st.text("Fixed Tax: 15,000")
            st.text("Tax % As Per Slab : 12.5%")
            taxperappinc=annual_taxable_amount-1200000
            #st.text("Tax %age Applied Income: "+str(taxperappinc))
            tax_as_per_slab=round((taxperappinc*12.5)/100)
            st.text("Tax As Per Slab: " + str(tax_as_per_slab))
            fixed_tax=15000
            total_yearly_tax=tax_as_per_slab+fixed_tax
            st.markdown(f'<p style=color:green>Annual Income Tax: {str(total_yearly_tax)}</p>',unsafe_allow_html=True)
            monthly_tax=round(total_yearly_tax/12)
            st.markdown(f"<p style=color:green>Monthly Income Tax: {str(monthly_tax)}</p>",unsafe_allow_html=True)
            tax_paid_this_year=round((total_yearly_tax/annual_taxable_amount)*100,4)
            st.markdown(f"<p style=color:green>Income Tax Ratio: {str(tax_paid_this_year)}%</p>",unsafe_allow_html=True)
        elif annual_taxable_amount>2400000 and annual_taxable_amount<=3600000:
            st.text("Fixed Tax: 165,000")
            st.text("Tax % As Per Slab: 22.5%")
            taxperappinc=annual_taxable_amount-2400000
            #st.text("Tax %age Applied Income: "+str(taxperappinc))
            tax_as_per_slab=round((taxperappinc*22.5)/100)
            st.text("Tax As Per Slab: " + str(tax_as_per_slab))
            fixed_tax=165000
            total_yearly_tax=tax_as_per_slab+fixed_tax
            st.markdown(f'<p style=color:green>Annual Income Tax: {str(total_yearly_tax)}</p>',unsafe_allow_html=True)
            monthly_tax=round(total_yearly_tax/12)
            st.markdown(f"<p style=color:green>Monthly Income Tax: {str(monthly_tax)}</p>",unsafe_allow_html=True)
            tax_paid_this_year=round((total_yearly_tax/annual_taxable_amount)*100,4)
            st.markdown(f"<p style=color:green>Income Tax Ratio: {str(tax_paid_this_year)}%</p>",unsafe_allow_html=True)
        elif annual_taxable_amount>3600000 and annual_taxable_amount<=6000000:
            st.text("Fixed Tax: 435,000")
            st.text("Tax % As Per Slab: 27.5%")
            taxperappinc=annual_taxable_amount-3600000
            #st.text("Tax %age Applied Income: "+str(taxperappinc))
            tax_as_per_slab=round((taxperappinc*27.5)/100)
            st.text("Tax As Per Slab: " + str(tax_as_per_slab))
            fixed_tax=435000
            total_yearly_tax=tax_as_per_slab+fixed_tax
            st.markdown(f'<p style=color:green>Annual Income Tax: {str(total_yearly_tax)}</p>',unsafe_allow_html=True)
            monthly_tax=round(total_yearly_tax/12)
            st.markdown(f"<p style=color:green>Monthly Income Tax: {str(monthly_tax)}</p>",unsafe_allow_html=True)
            tax_paid_this_year=round((total_yearly_tax/annual_taxable_amount)*100,4)
            st.markdown(f"<p style=color:green>Income Tax Ratio: {str(tax_paid_this_year)}%</p>",unsafe_allow_html=True)
        elif annual_taxable_amount>6000000:
            st.text("Fixed Tax: 1,095,000")
            st.text("Tax % As Per Slab: 35%")
            taxperappinc=annual_taxable_amount-6000000
            #st.text("Tax %age Applied Income: "+str(taxperappinc))
            tax_as_per_slab=round((taxperappinc*35.0)/100)
            st.text("Tax As Per Slab: " + str(tax_as_per_slab))
            fixed_tax=1095000
            total_yearly_tax=tax_as_per_slab+fixed_tax
            st.markdown(f'<p style=color:green>Annual Income Tax: {str(total_yearly_tax)}</p>',unsafe_allow_html=True)
            monthly_tax=round(total_yearly_tax/12)
            st.markdown(f"<p style=color:green>Monthly Income Tax: {str(monthly_tax)}</p>",unsafe_allow_html=True)
            tax_paid_this_year=round((total_yearly_tax/annual_taxable_amount)*100,4)
            st.markdown(f"<p style=color:green>Income Tax Ratio: {str(tax_paid_this_year)}%</p>",unsafe_allow_html=True)

identifying_slab_24()
