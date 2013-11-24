portscan
# 
# Script by Steven Grove (@sigwo)
#           www.sigwo.com
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

This is a TCP port scanner that automatically tries ports 0 - 65,536. I am not a coder, and this is probably very ugly to most of you. :-)

What it does:
Uses 'while' to loop through ports, writing results to a file called "results.csv". I am wanting to eventually get this to write to a database
of some sort, not sure which one yet.

How to use:
You will need Python 2.7 and the default libraries. Call "portscan.py" from the command line, input the IP or website you want to test (www.sigwo.com). 
As of now, there is no verification of what is entered. I am working on integrating the input checks.

On Windows, a cmd.exe window will appear, running the code through it. The lines are a way of showing it is still running and not hung. 

If you have questions, comments, or ideas, please email me. me@sigwo.com
